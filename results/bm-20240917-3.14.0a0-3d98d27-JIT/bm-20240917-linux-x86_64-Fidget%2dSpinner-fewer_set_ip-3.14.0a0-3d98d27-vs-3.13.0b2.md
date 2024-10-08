# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: fewer_set_ip
- machine: linux-x86_64
- commit hash: 3d98d27
- commit date: 2024-09-17
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                                    |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                  |
| html5lib       | 67.2 ms                                                    | 65.6 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 317 ms: 1.19x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 398 ms: 1.16x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                    |
| async_tree_io              | 939 ms                                                     | 863 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 877 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.1 ms: 1.14x faster                                                   |
| nbody          | 88.3 ms                                                    | 82.1 ms: 1.08x faster                                                   |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                   |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                    |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                    |
| regex_effbot   | 3.67 ms                                                    | 4.01 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                      | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 53.9 ms: 1.14x faster                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 77.5 ms: 1.13x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 144 ms: 1.12x faster                                                    |
| tomli_loads          | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 97.8 ms: 1.10x faster                                                   |
| json_loads           | 28.9 us                                                    | 27.0 us: 1.07x faster                                                   |
| pickle_dict          | 34.8 us                                                    | 33.0 us: 1.05x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                   |
| unpickle_list        | 5.34 us                                                    | 5.18 us: 1.03x faster                                                   |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                    |
| pickle_list          | 5.11 us                                                    | 5.02 us: 1.02x faster                                                   |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                            |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.80 ms: 1.15x faster                                                   |
| django_template | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 57.3 ms: 1.11x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.7 us: 1.49x faster                                                   |
| deepcopy                   | 367 us                                                     | 267 us: 1.38x faster                                                    |
| scimark_fft                | 392 ms                                                     | 301 ms: 1.31x faster                                                    |
| richards                   | 50.9 ms                                                    | 39.5 ms: 1.29x faster                                                   |
| richards_super             | 57.4 ms                                                    | 45.0 ms: 1.28x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                    | 2.63 us: 1.27x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.14 ms: 1.27x faster                                                   |
| async_tree_none            | 378 ms                                                     | 317 ms: 1.19x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 65.4 ms: 1.19x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 398 ms: 1.16x faster                                                    |
| mako                       | 11.2 ms                                                    | 9.80 ms: 1.15x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                    |
| float                      | 78.9 ms                                                    | 69.1 ms: 1.14x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 53.9 ms: 1.14x faster                                                   |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.13x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.43 sec: 1.13x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 77.5 ms: 1.13x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 144 ms: 1.12x faster                                                    |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 61.9 ms: 1.12x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 1.90 sec: 1.12x faster                                                  |
| go                         | 145 ms                                                     | 131 ms: 1.10x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 97.8 ms: 1.10x faster                                                   |
| coverage                   | 93.1 ms                                                    | 85.0 ms: 1.10x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                    |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                   |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                  |
| async_tree_io              | 939 ms                                                     | 863 ms: 1.09x faster                                                    |
| fannkuch                   | 402 ms                                                     | 369 ms: 1.09x faster                                                    |
| pyflate                    | 484 ms                                                     | 448 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                    |
| nbody                      | 88.3 ms                                                    | 82.1 ms: 1.08x faster                                                   |
| json_loads                 | 28.9 us                                                    | 27.0 us: 1.07x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.05 us: 1.07x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 877 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                                    |
| gc_traversal               | 3.98 ms                                                    | 3.74 ms: 1.06x faster                                                   |
| telco                      | 8.41 ms                                                    | 7.91 ms: 1.06x faster                                                   |
| sqlite_synth               | 2.99 us                                                    | 2.81 us: 1.06x faster                                                   |
| pickle_dict                | 34.8 us                                                    | 33.0 us: 1.05x faster                                                   |
| thrift                     | 823 us                                                     | 783 us: 1.05x faster                                                    |
| chaos                      | 61.3 ms                                                    | 58.6 ms: 1.05x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                   |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                                    |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                   |
| json                       | 5.31 ms                                                    | 5.12 ms: 1.04x faster                                                   |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                    |
| logging_silent             | 105 ns                                                     | 101 ns: 1.03x faster                                                    |
| unpickle_list              | 5.34 us                                                    | 5.18 us: 1.03x faster                                                   |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                                   |
| typing_runtime_protocols   | 165 us                                                     | 160 us: 1.03x faster                                                    |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 65.6 ms: 1.03x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 758 ms                                                     | 743 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                    |
| pickle_list                | 5.11 us                                                    | 5.02 us: 1.02x faster                                                   |
| asyncio_tcp                | 508 ms                                                     | 500 ms: 1.02x faster                                                    |
| deltablue                  | 3.25 ms                                                    | 3.21 ms: 1.01x faster                                                   |
| python_startup_no_site     | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                                   |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                   |
| bench_thread_pool          | 834 us                                                     | 836 us: 1.00x slower                                                    |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                                    |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                   |
| dulwich_log                | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                                   |
| django_template            | 34.8 ms                                                    | 35.2 ms: 1.01x slower                                                   |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                   |
| async_generators           | 442 ms                                                     | 453 ms: 1.02x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                                   |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                    |
| regex_dna                  | 221 ms                                                     | 228 ms: 1.03x slower                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                                   |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                                    |
| sqlglot_optimize           | 55.5 ms                                                    | 57.9 ms: 1.04x slower                                                   |
| nqueens                    | 81.4 ms                                                    | 85.0 ms: 1.04x slower                                                   |
| sympy_str                  | 282 ms                                                     | 295 ms: 1.05x slower                                                    |
| docutils                   | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                                  |
| sympy_expand               | 473 ms                                                     | 499 ms: 1.06x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.84 ms: 1.09x slower                                                   |
| regex_effbot               | 3.67 ms                                                    | 4.01 ms: 1.09x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 57.3 ms: 1.11x slower                                                   |
| generators                 | 29.6 ms                                                    | 33.3 ms: 1.12x slower                                                   |
| pylint                     | 317 ms                                                     | 371 ms: 1.17x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                            |

Benchmark hidden because not significant (5): pycparser, tornado_http, coroutines, pickle_pure_python, pprint_pformat
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240917-3.14.0a0-3d98d27-JIT/bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x