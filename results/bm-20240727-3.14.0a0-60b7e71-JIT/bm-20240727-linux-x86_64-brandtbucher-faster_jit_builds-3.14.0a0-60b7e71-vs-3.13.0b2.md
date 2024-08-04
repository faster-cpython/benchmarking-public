# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 271 ms: 1.01x faster                                                     |
| docutils       | 2.83 sec                                                   | 2.90 sec: 1.02x slower                                                   |
| html5lib       | 67.2 ms                                                    | 65.6 ms: 1.03x faster                                                    |
| tornado_http   | 94.6 ms                                                    | 92.9 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                      | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 413 ms: 1.12x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 528 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                     |
| async_tree_io              | 939 ms                                                     | 896 ms: 1.05x faster                                                     |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.0 ms: 1.13x faster                                                    |
| nbody          | 88.3 ms                                                    | 81.4 ms: 1.08x faster                                                    |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                      | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.03x faster                                                     |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.86 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 56.4 ms: 1.09x faster                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 80.7 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 99.5 ms: 1.08x faster                                                    |
| json_loads           | 28.9 us                                                    | 27.7 us: 1.04x faster                                                    |
| pickle_pure_python   | 305 us                                                     | 294 us: 1.04x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                    |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                     |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                    |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.95 ms: 1.13x faster                                                    |
| django_template | 34.8 ms                                                    | 35.4 ms: 1.02x slower                                                    |
| genshi_text     | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                    |
| genshi_xml      | 51.6 ms                                                    | 58.9 ms: 1.14x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.1 us: 1.41x faster                                                    |
| deepcopy                   | 367 us                                                     | 270 us: 1.36x faster                                                     |
| scimark_fft                | 392 ms                                                     | 308 ms: 1.28x faster                                                     |
| richards                   | 50.9 ms                                                    | 40.3 ms: 1.26x faster                                                    |
| richards_super             | 57.4 ms                                                    | 46.7 ms: 1.23x faster                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.31 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.78 us: 1.21x faster                                                    |
| spectral_norm              | 116 ms                                                     | 98.4 ms: 1.18x faster                                                    |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.2 ms: 1.15x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 67.4 ms: 1.15x faster                                                    |
| mako                       | 11.2 ms                                                    | 9.95 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 394 ms: 1.13x faster                                                     |
| float                      | 78.9 ms                                                    | 70.0 ms: 1.13x faster                                                    |
| pyflate                    | 484 ms                                                     | 431 ms: 1.12x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 413 ms: 1.12x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 528 ms: 1.11x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.53 sec: 1.11x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 56.4 ms: 1.09x faster                                                    |
| nbody                      | 88.3 ms                                                    | 81.4 ms: 1.08x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 80.7 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 99.5 ms: 1.08x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 868 ms: 1.08x faster                                                     |
| logging_format             | 6.47 us                                                    | 6.00 us: 1.08x faster                                                    |
| telco                      | 8.41 ms                                                    | 7.82 ms: 1.08x faster                                                    |
| fannkuch                   | 402 ms                                                     | 374 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 758 ms                                                     | 708 ms: 1.07x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.73 ms: 1.07x faster                                                    |
| chaos                      | 61.3 ms                                                    | 58.1 ms: 1.06x faster                                                    |
| meteor_contest             | 110 ms                                                     | 104 ms: 1.05x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.47 us: 1.05x faster                                                    |
| sqlglot_parse              | 1.32 ms                                                    | 1.26 ms: 1.05x faster                                                    |
| thrift                     | 823 us                                                     | 785 us: 1.05x faster                                                     |
| async_tree_io              | 939 ms                                                     | 896 ms: 1.05x faster                                                     |
| json_loads                 | 28.9 us                                                    | 27.7 us: 1.04x faster                                                    |
| pickle_pure_python         | 305 us                                                     | 294 us: 1.04x faster                                                     |
| generators                 | 29.6 ms                                                    | 28.5 ms: 1.04x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                    |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                                     |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                                    |
| regex_compile              | 137 ms                                                     | 132 ms: 1.03x faster                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                    |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.03x faster                                                    |
| html5lib                   | 67.2 ms                                                    | 65.6 ms: 1.03x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 496 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                     |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                    |
| coverage                   | 93.1 ms                                                    | 91.3 ms: 1.02x faster                                                    |
| tornado_http               | 94.6 ms                                                    | 92.9 ms: 1.02x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                    |
| dask                       | 369 ms                                                     | 364 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                     |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                     |
| 2to3                       | 274 ms                                                     | 271 ms: 1.01x faster                                                     |
| bench_thread_pool          | 834 us                                                     | 824 us: 1.01x faster                                                     |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                    |
| scimark_sor                | 127 ms                                                     | 128 ms: 1.00x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 55.8 ms: 1.00x slower                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                    |
| django_template            | 34.8 ms                                                    | 35.4 ms: 1.02x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.02x slower                                                     |
| docutils                   | 2.83 sec                                                   | 2.90 sec: 1.02x slower                                                   |
| regex_dna                  | 221 ms                                                     | 228 ms: 1.03x slower                                                     |
| scimark_lu                 | 122 ms                                                     | 126 ms: 1.03x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.55 ms: 1.04x slower                                                    |
| async_generators           | 442 ms                                                     | 461 ms: 1.04x slower                                                     |
| sympy_str                  | 282 ms                                                     | 295 ms: 1.05x slower                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.86 ms: 1.05x slower                                                    |
| sympy_expand               | 473 ms                                                     | 501 ms: 1.06x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 86.6 ms: 1.06x slower                                                    |
| deltablue                  | 3.25 ms                                                    | 3.48 ms: 1.07x slower                                                    |
| sympy_sum                  | 156 ms                                                     | 168 ms: 1.08x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 22.2 ms: 1.08x slower                                                    |
| pylint                     | 317 ms                                                     | 349 ms: 1.10x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 58.9 ms: 1.14x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                             |

Benchmark hidden because not significant (4): raytrace, regex_v8, pycparser, bench_mp_pool
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x