# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: 84bca09
- commit date: 2024-07-17
- overall geometric mean: 1.04x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 275 ms: 1.00x slower                                                 |
| docutils       | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                               |
| html5lib       | 67.2 ms                                                    | 63.3 ms: 1.06x faster                                                |
| tornado_http   | 94.6 ms                                                    | 93.2 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                      | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.17x faster                                                 |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 407 ms: 1.14x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                 |
| async_tree_io              | 939 ms                                                     | 846 ms: 1.11x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 844 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                                 |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                                |
| nbody          | 88.3 ms                                                    | 79.5 ms: 1.11x faster                                                |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                      | 1.09x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.82 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                      | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 79.6 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 98.6 ms: 1.09x faster                                                |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                               |
| xml_etree_process    | 61.2 ms                                                    | 56.8 ms: 1.08x faster                                                |
| json_loads           | 28.9 us                                                    | 27.6 us: 1.05x faster                                                |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                |
| pickle_pure_python   | 305 us                                                     | 293 us: 1.04x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.00x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.14 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                                |
| genshi_text     | 23.7 ms                                                    | 23.9 ms: 1.01x slower                                                |
| django_template | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                |
| genshi_xml      | 51.6 ms                                                    | 53.4 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-84bca09 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.7 us: 1.38x faster                                                |
| deepcopy                   | 367 us                                                     | 276 us: 1.33x faster                                                 |
| scimark_fft                | 392 ms                                                     | 309 ms: 1.27x faster                                                 |
| richards                   | 50.9 ms                                                    | 41.3 ms: 1.23x faster                                                |
| richards_super             | 57.4 ms                                                    | 47.2 ms: 1.22x faster                                                |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.35 ms: 1.21x faster                                                |
| deepcopy_reduce            | 3.35 us                                                    | 2.77 us: 1.21x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.17x faster                                                 |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                 |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                                |
| crypto_pyaes               | 77.5 ms                                                    | 67.9 ms: 1.14x faster                                                |
| async_tree_memoization     | 463 ms                                                     | 407 ms: 1.14x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.9 ms: 1.14x faster                                                |
| float                      | 78.9 ms                                                    | 70.2 ms: 1.12x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                 |
| fannkuch                   | 402 ms                                                     | 360 ms: 1.12x faster                                                 |
| pyflate                    | 484 ms                                                     | 434 ms: 1.11x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                 |
| nbody                      | 88.3 ms                                                    | 79.5 ms: 1.11x faster                                                |
| async_tree_io              | 939 ms                                                     | 846 ms: 1.11x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 844 ms: 1.11x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 79.6 ms: 1.10x faster                                                |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                |
| xml_etree_iterparse        | 107 ms                                                     | 98.6 ms: 1.09x faster                                                |
| gc_traversal               | 3.98 ms                                                    | 3.66 ms: 1.09x faster                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 541 ms: 1.09x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                               |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 564 ms: 1.08x faster                                                 |
| xml_etree_process          | 61.2 ms                                                    | 56.8 ms: 1.08x faster                                                |
| chaos                      | 61.3 ms                                                    | 57.5 ms: 1.07x faster                                                |
| html5lib                   | 67.2 ms                                                    | 63.3 ms: 1.06x faster                                                |
| logging_format             | 6.47 us                                                    | 6.12 us: 1.06x faster                                                |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                               |
| pprint_safe_repr           | 758 ms                                                     | 720 ms: 1.05x faster                                                 |
| telco                      | 8.41 ms                                                    | 8.03 ms: 1.05x faster                                                |
| json_loads                 | 28.9 us                                                    | 27.6 us: 1.05x faster                                                |
| logging_simple             | 5.74 us                                                    | 5.49 us: 1.05x faster                                                |
| bpe_tokeniser              | 5.02 sec                                                   | 4.81 sec: 1.05x faster                                               |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                |
| pickle_pure_python         | 305 us                                                     | 293 us: 1.04x faster                                                 |
| thrift                     | 823 us                                                     | 793 us: 1.04x faster                                                 |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                 |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                |
| json                       | 5.31 ms                                                    | 5.17 ms: 1.03x faster                                                |
| comprehensions             | 16.6 us                                                    | 16.2 us: 1.03x faster                                                |
| dask                       | 369 ms                                                     | 361 ms: 1.02x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                               |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                               |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 93.2 ms: 1.02x faster                                                |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                                 |
| bench_thread_pool          | 834 us                                                     | 828 us: 1.01x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.00x faster                                                 |
| 2to3                       | 274 ms                                                     | 275 ms: 1.00x slower                                                 |
| python_startup_no_site     | 7.11 ms                                                    | 7.14 ms: 1.00x slower                                                |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                |
| go                         | 145 ms                                                     | 145 ms: 1.01x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 23.9 ms: 1.01x slower                                                |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                                 |
| dulwich_log                | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                |
| docutils                   | 2.83 sec                                                   | 2.88 sec: 1.02x slower                                               |
| async_generators           | 442 ms                                                     | 450 ms: 1.02x slower                                                 |
| raytrace                   | 267 ms                                                     | 272 ms: 1.02x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                               |
| regex_v8                   | 25.1 ms                                                    | 25.7 ms: 1.02x slower                                                |
| django_template            | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                |
| regex_dna                  | 221 ms                                                     | 226 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                 |
| logging_silent             | 105 ns                                                     | 108 ns: 1.03x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 53.4 ms: 1.03x slower                                                |
| regex_effbot               | 3.67 ms                                                    | 3.82 ms: 1.04x slower                                                |
| sympy_str                  | 282 ms                                                     | 295 ms: 1.05x slower                                                 |
| sympy_expand               | 473 ms                                                     | 496 ms: 1.05x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 85.6 ms: 1.05x slower                                                |
| hexiom                     | 6.30 ms                                                    | 6.68 ms: 1.06x slower                                                |
| sympy_sum                  | 156 ms                                                     | 165 ms: 1.06x slower                                                 |
| pylint                     | 317 ms                                                     | 338 ms: 1.07x slower                                                 |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                                |
| deltablue                  | 3.25 ms                                                    | 3.65 ms: 1.12x slower                                                |
| generators                 | 29.6 ms                                                    | 45.4 ms: 1.53x slower                                                |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                         |

Benchmark hidden because not significant (4): coroutines, sqlglot_optimize, scimark_lu, coverage
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x