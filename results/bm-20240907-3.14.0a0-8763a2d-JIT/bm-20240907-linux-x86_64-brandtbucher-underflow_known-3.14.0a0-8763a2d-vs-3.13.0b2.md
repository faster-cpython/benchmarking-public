# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 8763a2d
- commit date: 2024-09-07
- overall geometric mean: 1.04x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 281 ms: 1.03x slower                                                   |
| docutils       | 2.83 sec                                                   | 3.01 sec: 1.06x slower                                                 |
| html5lib       | 67.2 ms                                                    | 61.9 ms: 1.09x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 396 ms: 1.17x faster                                                   |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 544 ms: 1.08x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 898 ms: 1.04x faster                                                   |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                           |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.1 ms: 1.13x faster                                                  |
| nbody          | 88.3 ms                                                    | 80.4 ms: 1.10x faster                                                  |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                      | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 213 ms: 1.04x faster                                                   |
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                  |
| regex_compile  | 137 ms                                                     | 146 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 76.9 ms: 1.14x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 54.4 ms: 1.13x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 198 us: 1.10x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 98.4 ms: 1.09x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                 |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.2 us: 1.02x faster                                                  |
| unpickle_list        | 5.34 us                                                    | 5.25 us: 1.02x faster                                                  |
| pickle_dict          | 34.8 us                                                    | 34.9 us: 1.00x slower                                                  |
| pickle_list          | 5.11 us                                                    | 5.30 us: 1.04x slower                                                  |
| pickle               | 11.5 us                                                    | 12.0 us: 1.05x slower                                                  |
| pickle_pure_python   | 305 us                                                     | 323 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                  |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                                  |
| genshi_text     | 23.7 ms                                                    | 23.9 ms: 1.01x slower                                                  |
| django_template | 34.8 ms                                                    | 35.7 ms: 1.03x slower                                                  |
| genshi_xml      | 51.6 ms                                                    | 54.1 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 25.2 us: 1.58x faster                                                  |
| deepcopy                   | 367 us                                                     | 267 us: 1.38x faster                                                   |
| richards_super             | 57.4 ms                                                    | 42.3 ms: 1.36x faster                                                  |
| richards                   | 50.9 ms                                                    | 37.8 ms: 1.35x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                                  |
| scimark_fft                | 392 ms                                                     | 316 ms: 1.24x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.49 ms: 1.17x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 396 ms: 1.17x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 66.5 ms: 1.17x faster                                                  |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                   |
| mako                       | 11.2 ms                                                    | 9.72 ms: 1.16x faster                                                  |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 76.9 ms: 1.14x faster                                                  |
| float                      | 78.9 ms                                                    | 70.1 ms: 1.13x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 54.4 ms: 1.13x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.48 sec: 1.12x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.59 ms: 1.11x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 198 us: 1.10x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                   |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.10x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.10x faster                                                  |
| nbody                      | 88.3 ms                                                    | 80.4 ms: 1.10x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                                 |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 98.4 ms: 1.09x faster                                                  |
| coverage                   | 93.1 ms                                                    | 85.4 ms: 1.09x faster                                                  |
| html5lib                   | 67.2 ms                                                    | 61.9 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 563 ms: 1.09x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.09x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                 |
| sqlite_synth               | 2.99 us                                                    | 2.77 us: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 544 ms: 1.08x faster                                                   |
| fannkuch                   | 402 ms                                                     | 373 ms: 1.08x faster                                                   |
| thrift                     | 823 us                                                     | 771 us: 1.07x faster                                                   |
| pyflate                    | 484 ms                                                     | 455 ms: 1.06x faster                                                   |
| telco                      | 8.41 ms                                                    | 7.97 ms: 1.06x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 482 ms: 1.05x faster                                                   |
| go                         | 145 ms                                                     | 139 ms: 1.04x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 898 ms: 1.04x faster                                                   |
| deltablue                  | 3.25 ms                                                    | 3.12 ms: 1.04x faster                                                  |
| regex_dna                  | 221 ms                                                     | 213 ms: 1.04x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.22 us: 1.04x faster                                                  |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                  |
| json_loads                 | 28.9 us                                                    | 28.2 us: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                 |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                   |
| unpickle_list              | 5.34 us                                                    | 5.25 us: 1.02x faster                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.67 us: 1.01x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 751 ms: 1.01x faster                                                   |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.7 ms: 1.01x faster                                                  |
| pickle_dict                | 34.8 us                                                    | 34.9 us: 1.00x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                  |
| genshi_text                | 23.7 ms                                                    | 23.9 ms: 1.01x slower                                                  |
| json                       | 5.31 ms                                                    | 5.38 ms: 1.01x slower                                                  |
| tornado_http               | 94.6 ms                                                    | 96.8 ms: 1.02x slower                                                  |
| 2to3                       | 274 ms                                                     | 281 ms: 1.03x slower                                                   |
| django_template            | 34.8 ms                                                    | 35.7 ms: 1.03x slower                                                  |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                   |
| pickle_list                | 5.11 us                                                    | 5.30 us: 1.04x slower                                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.70 ms: 1.04x slower                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.38 ms: 1.04x slower                                                  |
| async_generators           | 442 ms                                                     | 462 ms: 1.04x slower                                                   |
| pickle                     | 11.5 us                                                    | 12.0 us: 1.05x slower                                                  |
| genshi_xml                 | 51.6 ms                                                    | 54.1 ms: 1.05x slower                                                  |
| dulwich_log                | 67.2 ms                                                    | 70.8 ms: 1.05x slower                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 58.7 ms: 1.06x slower                                                  |
| pickle_pure_python         | 305 us                                                     | 323 us: 1.06x slower                                                   |
| nqueens                    | 81.4 ms                                                    | 86.2 ms: 1.06x slower                                                  |
| raytrace                   | 267 ms                                                     | 283 ms: 1.06x slower                                                   |
| docutils                   | 2.83 sec                                                   | 3.01 sec: 1.06x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.24 sec: 1.07x slower                                                 |
| regex_compile              | 137 ms                                                     | 146 ms: 1.07x slower                                                   |
| sympy_expand               | 473 ms                                                     | 508 ms: 1.07x slower                                                   |
| sympy_str                  | 282 ms                                                     | 306 ms: 1.09x slower                                                   |
| generators                 | 29.6 ms                                                    | 33.1 ms: 1.12x slower                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 77.3 ms: 1.12x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 23.0 ms: 1.12x slower                                                  |
| sympy_sum                  | 156 ms                                                     | 179 ms: 1.15x slower                                                   |
| pylint                     | 317 ms                                                     | 373 ms: 1.18x slower                                                   |
| hexiom                     | 6.30 ms                                                    | 7.72 ms: 1.23x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                           |

Benchmark hidden because not significant (7): pprint_pformat, unpickle, async_tree_io, comprehensions, typing_runtime_protocols, bench_thread_pool, chaos
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240907-3.14.0a0-8763a2d-JIT/bm-20240907-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-8763a2d.json: unpack_sequence

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x