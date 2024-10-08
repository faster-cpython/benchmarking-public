# Results vs. 3.13.0b2

- fork: python
- ref: 4ed7d1d6acc22807bfb5
- machine: linux-x86_64
- commit hash: 4ed7d1d
- commit date: 2024-09-12
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 254 ms: 1.08x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                                |
| html5lib       | 67.2 ms                                                    | 63.3 ms: 1.06x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 90.8 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 314 ms: 1.21x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 395 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 386 ms: 1.15x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                  |
| async_tree_io              | 939 ms                                                     | 864 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 554 ms: 1.06x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                  |
| nbody          | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                                 |
| float          | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                 |
| regex_dna      | 221 ms                                                     | 218 ms: 1.01x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 26.7 us: 1.08x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                 |
| unpickle_list        | 5.34 us                                                    | 5.17 us: 1.03x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 104 ms: 1.03x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 85.0 ms: 1.03x faster                                                 |
| pickle_dict          | 34.8 us                                                    | 33.9 us: 1.02x faster                                                 |
| tomli_loads          | 2.12 sec                                                   | 2.11 sec: 1.01x faster                                                |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                  |
| pickle_list          | 5.11 us                                                    | 5.14 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                 |
| django_template | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 50.9 ms: 1.01x faster                                                 |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 257 us: 1.43x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.7 us: 1.34x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.27x faster                                                 |
| go                         | 145 ms                                                     | 118 ms: 1.23x faster                                                  |
| async_tree_none            | 378 ms                                                     | 314 ms: 1.21x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 395 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 386 ms: 1.15x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.67 ms: 1.13x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                  |
| coverage                   | 93.1 ms                                                    | 84.6 ms: 1.10x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                 |
| richards_super             | 57.4 ms                                                    | 52.7 ms: 1.09x faster                                                 |
| richards                   | 50.9 ms                                                    | 46.8 ms: 1.09x faster                                                 |
| async_tree_io              | 939 ms                                                     | 864 ms: 1.09x faster                                                  |
| scimark_fft                | 392 ms                                                     | 362 ms: 1.08x faster                                                  |
| json_loads                 | 28.9 us                                                    | 26.7 us: 1.08x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 71.7 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                     | 254 ms: 1.08x faster                                                  |
| thrift                     | 823 us                                                     | 764 us: 1.08x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 472 ms: 1.08x faster                                                  |
| generators                 | 29.6 ms                                                    | 27.5 ms: 1.08x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                  |
| json                       | 5.31 ms                                                    | 4.96 ms: 1.07x faster                                                 |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                                  |
| logging_silent             | 105 ns                                                     | 98.2 ns: 1.07x faster                                                 |
| pyflate                    | 484 ms                                                     | 454 ms: 1.07x faster                                                  |
| docutils                   | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                                |
| html5lib                   | 67.2 ms                                                    | 63.3 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 554 ms: 1.06x faster                                                  |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                |
| bench_thread_pool          | 834 us                                                     | 792 us: 1.05x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 154 ms: 1.05x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.65 sec: 1.05x faster                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                 |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                                 |
| sympy_str                  | 282 ms                                                     | 269 ms: 1.05x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.80 sec: 1.05x faster                                                |
| pprint_safe_repr           | 758 ms                                                     | 725 ms: 1.05x faster                                                  |
| sympy_integrate            | 20.5 ms                                                    | 19.6 ms: 1.04x faster                                                 |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 53.2 ms: 1.04x faster                                                 |
| sqlite_synth               | 2.99 us                                                    | 2.87 us: 1.04x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 90.8 ms: 1.04x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.22 us: 1.04x faster                                                 |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                  |
| genshi_text                | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                 |
| dulwich_log                | 67.2 ms                                                    | 64.6 ms: 1.04x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                 |
| sympy_expand               | 473 ms                                                     | 456 ms: 1.04x faster                                                  |
| unpickle_list              | 5.34 us                                                    | 5.17 us: 1.03x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.03x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.1 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 104 ms: 1.03x faster                                                  |
| raytrace                   | 267 ms                                                     | 259 ms: 1.03x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 85.0 ms: 1.03x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                 |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| pickle_dict                | 34.8 us                                                    | 33.9 us: 1.02x faster                                                 |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.02x faster                                                |
| logging_simple             | 5.74 us                                                    | 5.61 us: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                  |
| async_generators           | 442 ms                                                     | 432 ms: 1.02x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                 |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                  |
| nbody                      | 88.3 ms                                                    | 86.5 ms: 1.02x faster                                                 |
| django_template            | 34.8 ms                                                    | 34.1 ms: 1.02x faster                                                 |
| hexiom                     | 6.30 ms                                                    | 6.17 ms: 1.02x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.3 us: 1.02x faster                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 6.99 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.01x faster                                                  |
| genshi_xml                 | 51.6 ms                                                    | 50.9 ms: 1.01x faster                                                 |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.01x faster                                                  |
| nqueens                    | 81.4 ms                                                    | 80.5 ms: 1.01x faster                                                 |
| fannkuch                   | 402 ms                                                     | 397 ms: 1.01x faster                                                  |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.22 ms: 1.01x faster                                                 |
| float                      | 78.9 ms                                                    | 78.1 ms: 1.01x faster                                                 |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 2.11 sec: 1.01x faster                                                |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| pickle_list                | 5.11 us                                                    | 5.14 us: 1.01x slower                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                 |
| telco                      | 8.41 ms                                                    | 8.53 ms: 1.01x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (5): unpickle, pickle, gc_traversal, coroutines, pylint
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-4ed7d1d/bm-20240912-linux-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x