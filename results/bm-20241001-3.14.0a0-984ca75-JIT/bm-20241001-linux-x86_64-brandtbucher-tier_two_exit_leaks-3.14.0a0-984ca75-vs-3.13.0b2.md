# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_exit_leaks
- machine: linux-x86_64
- commit hash: 984ca75
- commit date: 2024-10-01
- overall geometric mean: 1.03x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 279 ms: 1.02x slower                                                       |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                     |
| html5lib       | 67.2 ms                                                    | 66.2 ms: 1.02x faster                                                      |
| tornado_http   | 94.6 ms                                                    | 95.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 410 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 880 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 576 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 554 ms: 1.06x faster                                                       |
| async_tree_io              | 939 ms                                                     | 891 ms: 1.05x faster                                                       |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.5 ms: 1.10x faster                                                      |
| float          | 78.9 ms                                                    | 72.3 ms: 1.09x faster                                                      |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                      | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                      |
| regex_dna      | 221 ms                                                     | 222 ms: 1.00x slower                                                       |
| regex_compile  | 137 ms                                                     | 143 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                      | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.7 ms: 1.13x faster                                                      |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.11x faster                                                       |
| xml_etree_process    | 61.2 ms                                                    | 55.2 ms: 1.11x faster                                                      |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 97.5 ms: 1.10x faster                                                      |
| json_loads           | 28.9 us                                                    | 26.7 us: 1.08x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                      |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                                      |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                       |
| pickle_dict          | 34.8 us                                                    | 34.7 us: 1.00x faster                                                      |
| pickle_pure_python   | 305 us                                                     | 310 us: 1.01x slower                                                       |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                               |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                      |
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                                      |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                      |
| genshi_text     | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                                      |
| genshi_xml      | 51.6 ms                                                    | 59.2 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.0 us: 1.47x faster                                                      |
| deepcopy                   | 367 us                                                     | 271 us: 1.36x faster                                                       |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                       |
| richards_super             | 57.4 ms                                                    | 45.1 ms: 1.27x faster                                                      |
| richards                   | 50.9 ms                                                    | 40.0 ms: 1.27x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.67 us: 1.25x faster                                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.37 ms: 1.21x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 65.7 ms: 1.18x faster                                                      |
| async_tree_none            | 378 ms                                                     | 321 ms: 1.18x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                                      |
| bpe_tokeniser              | 5.02 sec                                                   | 4.42 sec: 1.14x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                                       |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 410 ms: 1.13x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 77.7 ms: 1.13x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.49 ms: 1.12x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.11x faster                                                       |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.11x faster                                                       |
| xml_etree_process          | 61.2 ms                                                    | 55.2 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.5 ms: 1.11x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.11x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 97.5 ms: 1.10x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                     |
| go                         | 145 ms                                                     | 132 ms: 1.10x faster                                                       |
| nbody                      | 88.3 ms                                                    | 80.5 ms: 1.10x faster                                                      |
| sqlite_synth               | 2.99 us                                                    | 2.74 us: 1.09x faster                                                      |
| coverage                   | 93.1 ms                                                    | 85.3 ms: 1.09x faster                                                      |
| float                      | 78.9 ms                                                    | 72.3 ms: 1.09x faster                                                      |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                       |
| json_loads                 | 28.9 us                                                    | 26.7 us: 1.08x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                       |
| fannkuch                   | 402 ms                                                     | 376 ms: 1.07x faster                                                       |
| async_tree_io_tg           | 936 ms                                                     | 880 ms: 1.06x faster                                                       |
| logging_format             | 6.47 us                                                    | 6.08 us: 1.06x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 576 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 554 ms: 1.06x faster                                                       |
| json                       | 5.31 ms                                                    | 5.02 ms: 1.06x faster                                                      |
| async_tree_io              | 939 ms                                                     | 891 ms: 1.05x faster                                                       |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                      |
| pyflate                    | 484 ms                                                     | 462 ms: 1.05x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.54 us: 1.04x faster                                                      |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 735 ms: 1.03x faster                                                       |
| regex_v8                   | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                      |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                       |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 494 ms: 1.03x faster                                                       |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                       |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                     |
| chaos                      | 61.3 ms                                                    | 60.0 ms: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                       |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                      |
| thrift                     | 823 us                                                     | 809 us: 1.02x faster                                                       |
| html5lib                   | 67.2 ms                                                    | 66.2 ms: 1.02x faster                                                      |
| deltablue                  | 3.25 ms                                                    | 3.21 ms: 1.01x faster                                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.65 ms: 1.01x faster                                                      |
| pickle_dict                | 34.8 us                                                    | 34.7 us: 1.00x faster                                                      |
| regex_dna                  | 221 ms                                                     | 222 ms: 1.00x slower                                                       |
| gc_traversal               | 3.98 ms                                                    | 3.99 ms: 1.00x slower                                                      |
| comprehensions             | 16.6 us                                                    | 16.8 us: 1.01x slower                                                      |
| dulwich_log                | 67.2 ms                                                    | 67.8 ms: 1.01x slower                                                      |
| tornado_http               | 94.6 ms                                                    | 95.7 ms: 1.01x slower                                                      |
| pickle_pure_python         | 305 us                                                     | 310 us: 1.01x slower                                                       |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                      |
| 2to3                       | 274 ms                                                     | 279 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                      |
| docutils                   | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                     |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                       |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                      |
| raytrace                   | 267 ms                                                     | 276 ms: 1.04x slower                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 1.70 ms: 1.04x slower                                                      |
| regex_compile              | 137 ms                                                     | 143 ms: 1.05x slower                                                       |
| sqlglot_normalize          | 110 ms                                                     | 117 ms: 1.06x slower                                                       |
| genshi_text                | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                                      |
| bench_thread_pool          | 834 us                                                     | 894 us: 1.07x slower                                                       |
| sympy_expand               | 473 ms                                                     | 508 ms: 1.07x slower                                                       |
| sympy_str                  | 282 ms                                                     | 305 ms: 1.08x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 88.6 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 60.5 ms: 1.09x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.92 ms: 1.10x slower                                                      |
| sympy_sum                  | 156 ms                                                     | 176 ms: 1.13x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 23.5 ms: 1.14x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 59.2 ms: 1.15x slower                                                      |
| generators                 | 29.6 ms                                                    | 34.9 ms: 1.18x slower                                                      |
| pylint                     | 317 ms                                                     | 374 ms: 1.18x slower                                                       |
| bench_mp_pool              | 23.9 ms                                                    | 60.7 ms: 2.54x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                               |

Benchmark hidden because not significant (6): unpickle_list, logging_silent, typing_runtime_protocols, pycparser, coroutines, pickle_list
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241001-3.14.0a0-984ca75-JIT/bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75.json: unpack_sequence

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x