# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: eb54546
- commit date: 2024-09-12
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                      |
| docutils       | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                    |
| html5lib       | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                                     |
| tornado_http   | 94.6 ms                                                    | 94.4 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                      | 1.00x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 316 ms: 1.20x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.17x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                      |
| async_tree_io              | 939 ms                                                     | 887 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 555 ms: 1.06x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                                     |
| nbody          | 88.3 ms                                                    | 80.9 ms: 1.09x faster                                                     |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                     |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                      |
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.86 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                      | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.0 ms: 1.13x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 54.4 ms: 1.13x faster                                                     |
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 9.96 ms: 1.08x faster                                                     |
| json_loads           | 28.9 us                                                    | 27.1 us: 1.07x faster                                                     |
| unpickle             | 15.1 us                                                    | 14.4 us: 1.05x faster                                                     |
| pickle_dict          | 34.8 us                                                    | 33.8 us: 1.03x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                      |
| pickle               | 11.5 us                                                    | 11.4 us: 1.00x faster                                                     |
| pickle_list          | 5.11 us                                                    | 5.08 us: 1.00x faster                                                     |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                              |

Benchmark hidden because not significant (2): unpickle_list, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.78 ms: 1.15x faster                                                     |
| genshi_text     | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                                     |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 56.8 ms: 1.10x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.9 us: 1.48x faster                                                     |
| deepcopy                   | 367 us                                                     | 259 us: 1.42x faster                                                      |
| richards                   | 50.9 ms                                                    | 39.7 ms: 1.28x faster                                                     |
| richards_super             | 57.4 ms                                                    | 45.1 ms: 1.27x faster                                                     |
| scimark_fft                | 392 ms                                                     | 311 ms: 1.26x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.25x faster                                                     |
| async_tree_none            | 378 ms                                                     | 316 ms: 1.20x faster                                                      |
| spectral_norm              | 116 ms                                                     | 97.4 ms: 1.19x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 394 ms: 1.17x faster                                                      |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.49 ms: 1.17x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 66.2 ms: 1.17x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.78 ms: 1.15x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 387 ms: 1.15x faster                                                      |
| bpe_tokeniser              | 5.02 sec                                                   | 4.41 sec: 1.14x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 77.0 ms: 1.13x faster                                                     |
| float                      | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 54.4 ms: 1.13x faster                                                     |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                      |
| coverage                   | 93.1 ms                                                    | 84.4 ms: 1.10x faster                                                     |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                                      |
| go                         | 145 ms                                                     | 132 ms: 1.10x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.2 ms: 1.09x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.09x faster                                                     |
| nbody                      | 88.3 ms                                                    | 80.9 ms: 1.09x faster                                                     |
| sqlite_synth               | 2.99 us                                                    | 2.76 us: 1.08x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                     |
| mdp                        | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                                    |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                      |
| pyflate                    | 484 ms                                                     | 449 ms: 1.08x faster                                                      |
| fannkuch                   | 402 ms                                                     | 373 ms: 1.08x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 9.96 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                      |
| json_loads                 | 28.9 us                                                    | 27.1 us: 1.07x faster                                                     |
| async_tree_io              | 939 ms                                                     | 887 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 555 ms: 1.06x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.12 us: 1.06x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.79 ms: 1.05x faster                                                     |
| thrift                     | 823 us                                                     | 784 us: 1.05x faster                                                      |
| unpickle                   | 15.1 us                                                    | 14.4 us: 1.05x faster                                                     |
| telco                      | 8.41 ms                                                    | 8.06 ms: 1.04x faster                                                     |
| chaos                      | 61.3 ms                                                    | 58.8 ms: 1.04x faster                                                     |
| html5lib                   | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                     |
| json                       | 5.31 ms                                                    | 5.13 ms: 1.03x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| pickle_dict                | 34.8 us                                                    | 33.8 us: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.61 us: 1.02x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 496 ms: 1.02x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 165 us                                                     | 161 us: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                    |
| deltablue                  | 3.25 ms                                                    | 3.20 ms: 1.02x faster                                                     |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.01x faster                                                     |
| pickle                     | 11.5 us                                                    | 11.4 us: 1.00x faster                                                     |
| pickle_list                | 5.11 us                                                    | 5.08 us: 1.00x faster                                                     |
| tornado_http               | 94.6 ms                                                    | 94.4 ms: 1.00x faster                                                     |
| bench_thread_pool          | 834 us                                                     | 837 us: 1.00x slower                                                      |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                      |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                     |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.01x slower                                                      |
| dulwich_log                | 67.2 ms                                                    | 68.3 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                                     |
| regex_compile              | 137 ms                                                     | 140 ms: 1.02x slower                                                      |
| genshi_text                | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                                     |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                                      |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                     |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 57.8 ms: 1.04x slower                                                     |
| docutils                   | 2.83 sec                                                   | 2.95 sec: 1.04x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 85.1 ms: 1.05x slower                                                     |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.86 ms: 1.05x slower                                                     |
| sympy_expand               | 473 ms                                                     | 500 ms: 1.06x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.78 ms: 1.08x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 22.6 ms: 1.10x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 56.8 ms: 1.10x slower                                                     |
| generators                 | 29.6 ms                                                    | 32.9 ms: 1.11x slower                                                     |
| pylint                     | 317 ms                                                     | 372 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                              |

Benchmark hidden because not significant (5): pprint_pformat, pycparser, pprint_safe_repr, unpickle_list, pickle_pure_python
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-eb54546-JIT/bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x