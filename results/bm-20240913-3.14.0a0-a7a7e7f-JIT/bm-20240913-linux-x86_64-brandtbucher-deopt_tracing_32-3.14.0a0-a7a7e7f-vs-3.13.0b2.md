# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: deopt_tracing_32
- machine: linux-x86_64
- commit hash: a7a7e7f
- commit date: 2024-09-13
- overall geometric mean: 1.04x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                    |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                  |
| html5lib       | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                    |
| async_tree_io              | 939 ms                                                     | 852 ms: 1.10x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.4 ms: 1.14x faster                                                   |
| nbody          | 88.3 ms                                                    | 81.9 ms: 1.08x faster                                                   |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 221 ms: 1.00x faster                                                    |
| regex_effbot   | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                   |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.5 ms: 1.13x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                                   |
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 99.7 ms: 1.08x faster                                                   |
| json_loads           | 28.9 us                                                    | 27.1 us: 1.07x faster                                                   |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.07x faster                                                   |
| pickle_dict          | 34.8 us                                                    | 33.2 us: 1.05x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                    |
| pickle_list          | 5.11 us                                                    | 5.04 us: 1.01x faster                                                   |
| pickle               | 11.5 us                                                    | 11.3 us: 1.01x faster                                                   |
| unpickle_list        | 5.34 us                                                    | 5.30 us: 1.01x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.01x faster                                                    |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                   |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 59.4 ms: 1.15x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.0 us: 1.47x faster                                                   |
| deepcopy                   | 367 us                                                     | 264 us: 1.39x faster                                                    |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.62 us: 1.28x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.21 ms: 1.25x faster                                                   |
| richards                   | 50.9 ms                                                    | 41.1 ms: 1.24x faster                                                   |
| richards_super             | 57.4 ms                                                    | 47.3 ms: 1.21x faster                                                   |
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 65.3 ms: 1.19x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.17x faster                                                    |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                                    |
| mako                       | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                    |
| float                      | 78.9 ms                                                    | 69.4 ms: 1.14x faster                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 77.5 ms: 1.13x faster                                                   |
| bpe_tokeniser              | 5.02 sec                                                   | 4.45 sec: 1.13x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.6 ms: 1.10x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.52 sec: 1.10x faster                                                  |
| async_tree_io              | 939 ms                                                     | 852 ms: 1.10x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.10x faster                                                    |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                    |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                    |
| gc_traversal               | 3.98 ms                                                    | 3.65 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                    |
| sqlite_synth               | 2.99 us                                                    | 2.77 us: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 99.7 ms: 1.08x faster                                                   |
| nbody                      | 88.3 ms                                                    | 81.9 ms: 1.08x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 869 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                    |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.07x faster                                                   |
| go                         | 145 ms                                                     | 135 ms: 1.07x faster                                                    |
| json                       | 5.31 ms                                                    | 4.95 ms: 1.07x faster                                                   |
| json_loads                 | 28.9 us                                                    | 27.1 us: 1.07x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.07x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.10 us: 1.06x faster                                                   |
| telco                      | 8.41 ms                                                    | 7.93 ms: 1.06x faster                                                   |
| fannkuch                   | 402 ms                                                     | 380 ms: 1.06x faster                                                    |
| pyflate                    | 484 ms                                                     | 458 ms: 1.06x faster                                                    |
| pprint_safe_repr           | 758 ms                                                     | 720 ms: 1.05x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                                   |
| pickle_dict                | 34.8 us                                                    | 33.2 us: 1.05x faster                                                   |
| thrift                     | 823 us                                                     | 789 us: 1.04x faster                                                    |
| coverage                   | 93.1 ms                                                    | 89.6 ms: 1.04x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                   |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                    |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                    |
| logging_simple             | 5.74 us                                                    | 5.58 us: 1.03x faster                                                   |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                   |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                    |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 498 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| pickle_list                | 5.11 us                                                    | 5.04 us: 1.01x faster                                                   |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                   |
| pickle                     | 11.5 us                                                    | 11.3 us: 1.01x faster                                                   |
| unpickle_list              | 5.34 us                                                    | 5.30 us: 1.01x faster                                                   |
| dulwich_log                | 67.2 ms                                                    | 66.7 ms: 1.01x faster                                                   |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.01x faster                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                   |
| regex_dna                  | 221 ms                                                     | 221 ms: 1.00x faster                                                    |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                   |
| regex_effbot               | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                   |
| 2to3                       | 274 ms                                                     | 279 ms: 1.02x slower                                                    |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                   |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                    |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                   |
| raytrace                   | 267 ms                                                     | 276 ms: 1.03x slower                                                    |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 84.8 ms: 1.04x slower                                                   |
| docutils                   | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                  |
| pycparser                  | 1.16 sec                                                   | 1.21 sec: 1.05x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.72 ms: 1.05x slower                                                   |
| genshi_text                | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 59.0 ms: 1.06x slower                                                   |
| coroutines                 | 23.2 ms                                                    | 24.9 ms: 1.07x slower                                                   |
| sympy_str                  | 282 ms                                                     | 305 ms: 1.08x slower                                                    |
| deltablue                  | 3.25 ms                                                    | 3.55 ms: 1.09x slower                                                   |
| sympy_expand               | 473 ms                                                     | 517 ms: 1.09x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.89 ms: 1.09x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 174 ms: 1.12x slower                                                    |
| generators                 | 29.6 ms                                                    | 33.2 ms: 1.12x slower                                                   |
| sympy_integrate            | 20.5 ms                                                    | 23.0 ms: 1.12x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 59.4 ms: 1.15x slower                                                   |
| pylint                     | 317 ms                                                     | 379 ms: 1.20x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                            |

Benchmark hidden because not significant (4): tornado_http, regex_v8, bench_thread_pool, unpickle
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240913-3.14.0a0-a7a7e7f-JIT/bm-20240913-linux-x86_64-brandtbucher-deopt_tracing_32-3.14.0a0-a7a7e7f.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x