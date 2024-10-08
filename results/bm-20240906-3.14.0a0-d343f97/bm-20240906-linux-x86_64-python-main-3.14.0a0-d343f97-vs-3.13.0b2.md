# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d343f97
- commit date: 2024-09-06
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                     | 256 ms: 1.07x faster                                  |
| docutils       | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                |
| html5lib       | 67.2 ms                                                    | 62.2 ms: 1.08x faster                                 |
| tornado_http   | 94.6 ms                                                    | 91.6 ms: 1.03x faster                                 |
| Geometric mean | (ref)                                                      | 1.06x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 387 ms: 1.20x faster                                  |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 398 ms: 1.11x faster                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                  |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.10x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 892 ms: 1.05x faster                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                  |
| nbody          | 88.3 ms                                                    | 86.3 ms: 1.02x faster                                 |
| float          | 78.9 ms                                                    | 77.8 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 128 ms: 1.07x faster                                  |
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                 |
| regex_effbot   | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                 |
| regex_dna      | 221 ms                                                     | 223 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                      | 1.03x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                 |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                  |
| xml_etree_generate   | 87.4 ms                                                    | 85.2 ms: 1.03x faster                                 |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                 |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                  |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                |
| unpickle_list        | 5.34 us                                                    | 5.25 us: 1.02x faster                                 |
| json_loads           | 28.9 us                                                    | 28.4 us: 1.02x faster                                 |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                  |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.01x faster                                  |
| pickle_list          | 5.11 us                                                    | 5.16 us: 1.01x slower                                 |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                 |
| pickle_dict          | 34.8 us                                                    | 35.4 us: 1.02x slower                                 |
| Geometric mean       | (ref)                                                      | 1.01x faster                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.1 ms: 1.07x faster                                 |
| genshi_xml      | 51.6 ms                                                    | 48.7 ms: 1.06x faster                                 |
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                 |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                 |
| Geometric mean  | (ref)                                                      | 1.04x faster                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 258 us: 1.42x faster                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.7 us: 1.34x faster                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                 |
| go                         | 145 ms                                                     | 118 ms: 1.23x faster                                  |
| async_tree_memoization     | 463 ms                                                     | 387 ms: 1.20x faster                                  |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                  |
| gc_traversal               | 3.98 ms                                                    | 3.56 ms: 1.12x faster                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 398 ms: 1.11x faster                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                  |
| async_tree_none_tg         | 336 ms                                                     | 306 ms: 1.10x faster                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 536 ms: 1.10x faster                                  |
| richards                   | 50.9 ms                                                    | 46.5 ms: 1.10x faster                                 |
| richards_super             | 57.4 ms                                                    | 52.5 ms: 1.09x faster                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.83 ms: 1.09x faster                                 |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                 |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.09x faster                                  |
| scimark_fft                | 392 ms                                                     | 363 ms: 1.08x faster                                  |
| html5lib                   | 67.2 ms                                                    | 62.2 ms: 1.08x faster                                 |
| coverage                   | 93.1 ms                                                    | 86.6 ms: 1.08x faster                                 |
| 2to3                       | 274 ms                                                     | 256 ms: 1.07x faster                                  |
| regex_compile              | 137 ms                                                     | 128 ms: 1.07x faster                                  |
| genshi_text                | 23.7 ms                                                    | 22.1 ms: 1.07x faster                                 |
| generators                 | 29.6 ms                                                    | 27.8 ms: 1.07x faster                                 |
| thrift                     | 823 us                                                     | 772 us: 1.07x faster                                  |
| docutils                   | 2.83 sec                                                   | 2.66 sec: 1.06x faster                                |
| pprint_safe_repr           | 758 ms                                                     | 713 ms: 1.06x faster                                  |
| crypto_pyaes               | 77.5 ms                                                    | 73.1 ms: 1.06x faster                                 |
| genshi_xml                 | 51.6 ms                                                    | 48.7 ms: 1.06x faster                                 |
| asyncio_tcp                | 508 ms                                                     | 481 ms: 1.06x faster                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.72 ms: 1.06x faster                                 |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                |
| bench_thread_pool          | 834 us                                                     | 790 us: 1.06x faster                                  |
| sympy_str                  | 282 ms                                                     | 268 ms: 1.05x faster                                  |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.05x faster                                  |
| async_tree_io_tg           | 936 ms                                                     | 892 ms: 1.05x faster                                  |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                 |
| sympy_integrate            | 20.5 ms                                                    | 19.6 ms: 1.05x faster                                 |
| xml_etree_process          | 61.2 ms                                                    | 58.6 ms: 1.04x faster                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.3 ms: 1.04x faster                                 |
| dulwich_log                | 67.2 ms                                                    | 64.6 ms: 1.04x faster                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                  |
| typing_runtime_protocols   | 165 us                                                     | 159 us: 1.03x faster                                  |
| sympy_expand               | 473 ms                                                     | 457 ms: 1.03x faster                                  |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                  |
| logging_format             | 6.47 us                                                    | 6.26 us: 1.03x faster                                 |
| tornado_http               | 94.6 ms                                                    | 91.6 ms: 1.03x faster                                 |
| sqlite_synth               | 2.99 us                                                    | 2.89 us: 1.03x faster                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.4 ms: 1.03x faster                                 |
| xml_etree_generate         | 87.4 ms                                                    | 85.2 ms: 1.03x faster                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.03x faster                                 |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                 |
| hexiom                     | 6.30 ms                                                    | 6.14 ms: 1.03x faster                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.03x faster                                |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                  |
| raytrace                   | 267 ms                                                     | 260 ms: 1.02x faster                                  |
| nbody                      | 88.3 ms                                                    | 86.3 ms: 1.02x faster                                 |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                 |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                  |
| pyflate                    | 484 ms                                                     | 475 ms: 1.02x faster                                  |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                  |
| tomli_loads                | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                  |
| unpickle_list              | 5.34 us                                                    | 5.25 us: 1.02x faster                                 |
| json_loads                 | 28.9 us                                                    | 28.4 us: 1.02x faster                                 |
| django_template            | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                 |
| telco                      | 8.41 ms                                                    | 8.27 ms: 1.02x faster                                 |
| spectral_norm              | 116 ms                                                     | 114 ms: 1.02x faster                                  |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                 |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                  |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                  |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                 |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                  |
| deltablue                  | 3.25 ms                                                    | 3.21 ms: 1.01x faster                                 |
| float                      | 78.9 ms                                                    | 77.8 ms: 1.01x faster                                 |
| regex_effbot               | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                 |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.01x faster                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                 |
| async_generators           | 442 ms                                                     | 439 ms: 1.01x faster                                  |
| nqueens                    | 81.4 ms                                                    | 81.2 ms: 1.00x faster                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                 |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                 |
| regex_dna                  | 221 ms                                                     | 223 ms: 1.01x slower                                  |
| json                       | 5.31 ms                                                    | 5.35 ms: 1.01x slower                                 |
| pickle_list                | 5.11 us                                                    | 5.16 us: 1.01x slower                                 |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                 |
| pickle_dict                | 34.8 us                                                    | 35.4 us: 1.02x slower                                 |
| fannkuch                   | 402 ms                                                     | 410 ms: 1.02x slower                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                          |

Benchmark hidden because not significant (6): async_tree_io, pycparser, coroutines, logging_simple, unpickle, pylint
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240906-3.14.0a0-d343f97/bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x