# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: e666b14
- commit date: 2024-09-08
- overall geometric mean: 1.02x faster
- HPT reliability: 98.20%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 288 ms: 1.05x slower                                                        |
| docutils       | 2.83 sec                                                   | 3.23 sec: 1.14x slower                                                      |
| html5lib       | 67.2 ms                                                    | 67.7 ms: 1.01x slower                                                       |
| tornado_http   | 94.6 ms                                                    | 104 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                      | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 416 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 412 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 317 ms: 1.06x faster                                                        |
| async_tree_io_tg           | 936 ms                                                     | 910 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                      | 1.07x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.4 ms: 1.10x faster                                                       |
| nbody          | 88.3 ms                                                    | 80.7 ms: 1.09x faster                                                       |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                      | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 212 ms: 1.05x faster                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                                       |
| regex_v8       | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                                       |
| regex_compile  | 137 ms                                                     | 154 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 53.9 ms: 1.14x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 77.2 ms: 1.13x faster                                                       |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                     | 98.3 ms: 1.09x faster                                                       |
| unpickle_pure_python | 218 us                                                     | 201 us: 1.09x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| tomli_loads          | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                                      |
| unpickle_list        | 5.34 us                                                    | 5.24 us: 1.02x faster                                                       |
| pickle_dict          | 34.8 us                                                    | 34.7 us: 1.00x faster                                                       |
| pickle_list          | 5.11 us                                                    | 5.29 us: 1.04x slower                                                       |
| pickle_pure_python   | 305 us                                                     | 330 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                                |

Benchmark hidden because not significant (3): unpickle, json_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.75 ms: 1.15x faster                                                       |
| genshi_text     | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                       |
| django_template | 34.8 ms                                                    | 37.8 ms: 1.09x slower                                                       |
| genshi_xml      | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 25.2 us: 1.57x faster                                                       |
| deepcopy                   | 367 us                                                     | 267 us: 1.37x faster                                                        |
| richards_super             | 57.4 ms                                                    | 44.3 ms: 1.29x faster                                                       |
| richards                   | 50.9 ms                                                    | 39.4 ms: 1.29x faster                                                       |
| scimark_fft                | 392 ms                                                     | 311 ms: 1.26x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.24x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.41 ms: 1.20x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 66.5 ms: 1.16x faster                                                       |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                                        |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                        |
| mako                       | 11.2 ms                                                    | 9.75 ms: 1.15x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 53.9 ms: 1.14x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 77.2 ms: 1.13x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 416 ms: 1.11x faster                                                        |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.11x faster                                                        |
| float                      | 78.9 ms                                                    | 71.4 ms: 1.10x faster                                                       |
| bpe_tokeniser              | 5.02 sec                                                   | 4.55 sec: 1.10x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.10x faster                                                        |
| nbody                      | 88.3 ms                                                    | 80.7 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                     | 98.3 ms: 1.09x faster                                                       |
| coverage                   | 93.1 ms                                                    | 85.2 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                        |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                       |
| sqlite_synth               | 2.99 us                                                    | 2.75 us: 1.09x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 201 us: 1.09x faster                                                        |
| fannkuch                   | 402 ms                                                     | 373 ms: 1.08x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 412 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 547 ms: 1.07x faster                                                        |
| go                         | 145 ms                                                     | 135 ms: 1.07x faster                                                        |
| chaos                      | 61.3 ms                                                    | 57.5 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 317 ms: 1.06x faster                                                        |
| pyflate                    | 484 ms                                                     | 458 ms: 1.06x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.77 ms: 1.05x faster                                                       |
| thrift                     | 823 us                                                     | 782 us: 1.05x faster                                                        |
| scimark_sor                | 127 ms                                                     | 121 ms: 1.05x faster                                                        |
| telco                      | 8.41 ms                                                    | 8.02 ms: 1.05x faster                                                       |
| regex_dna                  | 221 ms                                                     | 212 ms: 1.05x faster                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                       |
| genshi_text                | 23.7 ms                                                    | 22.8 ms: 1.04x faster                                                       |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 910 ms: 1.03x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                       |
| tomli_loads                | 2.12 sec                                                   | 2.07 sec: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.59 ms: 1.02x faster                                                       |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                        |
| unpickle_list              | 5.34 us                                                    | 5.24 us: 1.02x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 746 ms: 1.02x faster                                                        |
| logging_format             | 6.47 us                                                    | 6.36 us: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| asyncio_tcp                | 508 ms                                                     | 506 ms: 1.00x faster                                                        |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.00x faster                                                       |
| pickle_dict                | 34.8 us                                                    | 34.7 us: 1.00x faster                                                       |
| bench_thread_pool          | 834 us                                                     | 837 us: 1.00x slower                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                       |
| html5lib                   | 67.2 ms                                                    | 67.7 ms: 1.01x slower                                                       |
| deltablue                  | 3.25 ms                                                    | 3.28 ms: 1.01x slower                                                       |
| regex_v8                   | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                       |
| json                       | 5.31 ms                                                    | 5.36 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                        |
| async_generators           | 442 ms                                                     | 452 ms: 1.02x slower                                                        |
| logging_simple             | 5.74 us                                                    | 5.89 us: 1.02x slower                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 71.4 ms: 1.03x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 84.0 ms: 1.03x slower                                                       |
| pickle_list                | 5.11 us                                                    | 5.29 us: 1.04x slower                                                       |
| logging_silent             | 105 ns                                                     | 109 ns: 1.05x slower                                                        |
| 2to3                       | 274 ms                                                     | 288 ms: 1.05x slower                                                        |
| raytrace                   | 267 ms                                                     | 284 ms: 1.06x slower                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.75 ms: 1.07x slower                                                       |
| pickle_pure_python         | 305 us                                                     | 330 us: 1.08x slower                                                        |
| django_template            | 34.8 ms                                                    | 37.8 ms: 1.09x slower                                                       |
| tornado_http               | 94.6 ms                                                    | 104 ms: 1.10x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 121 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 61.6 ms: 1.11x slower                                                       |
| generators                 | 29.6 ms                                                    | 33.2 ms: 1.12x slower                                                       |
| dulwich_log                | 67.2 ms                                                    | 75.4 ms: 1.12x slower                                                       |
| regex_compile              | 137 ms                                                     | 154 ms: 1.13x slower                                                        |
| sympy_expand               | 473 ms                                                     | 533 ms: 1.13x slower                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.49 ms: 1.13x slower                                                       |
| genshi_xml                 | 51.6 ms                                                    | 58.7 ms: 1.14x slower                                                       |
| sympy_str                  | 282 ms                                                     | 322 ms: 1.14x slower                                                        |
| pycparser                  | 1.16 sec                                                   | 1.32 sec: 1.14x slower                                                      |
| docutils                   | 2.83 sec                                                   | 3.23 sec: 1.14x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 7.42 ms: 1.18x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 24.9 ms: 1.21x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 190 ms: 1.22x slower                                                        |
| pylint                     | 317 ms                                                     | 412 ms: 1.30x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                                |

Benchmark hidden because not significant (4): unpickle, async_tree_io, json_loads, pickle
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240908-3.14.0a0-e666b14-JIT/bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14.json: unpack_sequence

# HPT report

- Reliability score: 98.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x